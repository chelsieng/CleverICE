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

  getRequestName(argumentName?: typedef): Observable<returnTypeDef> {
    let url = '/xxxxx/';
    // some operations here
    return this.http.get<returnTypeDef>(url);
  }

  uploadImage(filename: any): Observable<returnTypeDef> {
    const url = '/uploadImage';
    return this.http.post<returnTypeDef>(url, filename);
  }
}
