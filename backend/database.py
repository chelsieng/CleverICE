"""This module performs the following steps sequentially:
    1. Reads in existing account IDs (if any) from the bank database.
    2. Creates additional accounts with randomly generated IDs. Then, it adds a bit of money to each new account.
    3. Chooses two accounts at random and takes half of the money from the first and deposits it into the second.
"""

from hashlib import md5
from time import localtime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cockroachdb.sqlalchemy import run_transaction

Base = declarative_base()

class Document(Base):
    """The Document class corresponds to the "document" database table.
    """
    __tablename__ = 'document'
    document_id = Column(String, primary_key=True)
    user_id = Column(String)
    document_name = Column(String)
    path_to_pdf = Column(String)
    path_to_text = Column(String)

class UserAccounts(Base):
    """The User class corresponds to the "user" database table.
    """
    __tablename__ = 'user_accounts'
    user_id = Column(String, primary_key=True)
    username = Column(String)
    password = Column(String)

# Create an engine to communicate with the database. The
# "cockroachdb://" prefix for the engine URL indicates that we are
# connecting to CockroachDB using the 'cockroachdb' dialect.
# For more information, see
# https://github.com/cockroachdb/sqlalchemy-cockroachdb.

engine = create_engine(
    # For cockroach demo:
    # 'cockroachdb://<username>:<password>@<hostname>:<port>/bank?sslmode=require',
    # For CockroachCloud:
    'cockroachdb://duc:iloveconcordia@free-tier5.gcp-europe-west1.cockroachlabs.cloud:26257/defaultdb?&sslmode=require&options=--cluster=young-cougar-295',
    # 'cockroachdb://<username>:<password>@<globalhost>:26257/<cluster_name>.bank?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>',
    echo=True                   # Log SQL queries to stdout
)

# Automatically create the "accounts" table based on the Account class.
Base.metadata.create_all(engine)

# Store the account IDs we create for later use.
seen_account_ids = set()


def create_init_users():
    """ Generate random IDs for new accounts.
    """

    def method(sess):
        new_users = []

        new_users.append(
            UserAccounts(
                user_id = 'user-11',
                username = 'niyonx',
                password = 'password',
            )
        )

        new_users.append(
            UserAccounts(
                user_id = 'user-22',
                username = 'duc',
                password = 'pw',
            )
        )

        sess.add_all(new_users)

    return run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))

def get_documents():
    """ Get all the documents exist.
    """

    def method(sess):
        result = []
        for instance in sess.query(Document).all():
            result.append({
                'document_id':instance.document_id,
                'document_name':instance.document_name,
                'path_to_pdf':instance.path_to_pdf,
                'path_to_text':instance.path_to_text
            }
          )

        return tuple(result)

    return run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))

def create_document(document_name, path_to_pdf, path_to_text, user_id):

    def method(sess):
        new_document = []
        # Create unique id by hashing the current time.
        new_id = 'doc-' + md5(str(localtime()).encode('utf-8')).hexdigest()
        new_document.append(
            Document(
                user_id=user_id,
                document_id=new_id,
                document_name=document_name,
                path_to_pdf=path_to_pdf,
                path_to_text=path_to_text
            )
        )

        sess.add_all(new_document)

    run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))
    
    return '200'

def delete_document(id):
    def method(sess):
        sess.query(Document).filter(Document.document_id == id).delete()
        return True

    run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))
    
    return '200'

def create_user(username, password):

    def method(sess):
        new_user = []

        # Create unique id by hashing local time.
        new_id = 'user-' + md5(str(localtime()).encode('utf-8')).hexdigest()

        new_user.append(
            UserAccounts(
                user_id = new_id,
                username = username,
                password = password,
            )
        )

        sess.add_all(new_user)

    run_transaction(sessionmaker(bind=engine),
                lambda s: method(s))
    
    return '200'

def total_documents():
    """ Count the number of documents.
    """
    def method(sess):
        return str(sess.query(Document).count())

    return run_transaction(sessionmaker(bind=engine),lambda s: method(s))

def check_user(username, password):
    """ Verify username and password
    """
    def method(sess):
        user = sess.query(UserAccounts).filter_by(username=username).first()

        if(user and user.password == password):
            return '200' # access allowed.
        return '403' # reject access.

    
    return run_transaction(sessionmaker(bind=engine),lambda s: method(s))


"""
# Testing:

create_init_users()
create_document('health_claim', 'pdfPath/health_claim.pdf', 'pdf_results/health_claim_output-1-to-1.json', 'user-11')
create_document('auto_claim', 'pdfPath/auto_claim.pdf', 'pdf_results/auto_claim_output-1-to-1.json', 'user-22')
create_user('Chelsie', 'password')

"""