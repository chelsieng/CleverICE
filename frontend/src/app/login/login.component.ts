import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  focus;
  focus1;
  api;

  constructor(api: ApiService) {
    this.api = api
  }



  ngOnInit() {
  }

}
