import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private http: HttpClient;

  constructor(http: HttpClient) {
    this.http = http;
  }

  getScan(filename?: string): Observable<string> {
    let url = '/scan_filename/' + filename;
    return this.http.get<string>(url);
  }

  uploadImage(filename: any): Observable<any> {
    filename = filename.replace(/.*[\/\\]/, '')
    const url = '/uploadblob/' + filename;
    return this.http.get<any>(url);
  }


  scanFilename(filename: any): Observable<any> {
    filename = filename.replace(/.*[\/\\]/, '')
    const url = '/scan_filename/'+filename;
    return this.http.get<any>(url);
  }

  registerUser(email: string, password: string): Observable<any> {
    const url = '/createUser';
    return this.http.post<any>(url, [email, password]);
  }
}
