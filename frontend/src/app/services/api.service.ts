import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private http: HttpClient;

  constructor(http: HttpClient) {
    this.http = http;
  }

  // Functions Example

  // getRequestName(argumentName?: typedef): Observable<returnTypeDef> {
  //   let url = '/xxxxx/';
  //   // some operations here
  //   return this.http.get<returnTypeDef>(url);
  // }

  // postRequestName(argumentName: typedef): Observable<returnTypeDef> {
  //   const url = '/xxxxx';
  //   return this.http.post<returnTypeDef>(url, argumentName);
  // }
}
