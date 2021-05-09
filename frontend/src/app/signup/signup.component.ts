import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
    selector: 'app-signup',
    templateUrl: './signup.component.html',
    styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {
    test : Date = new Date();
    focus;
    focus1;
    focus2;
    api;

    constructor(api: ApiService) {
      this.api = api;
    }

    registerUser(email: string, password: string) {
      this.api.registerUser(email, password).subscribe(
        (data: any) => {
          console.log(data)
        },
        (err: HttpErrorResponse) => console.error(err),
      );
    }

    ngOnInit() {}
}
