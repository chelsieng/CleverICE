import {Component, OnInit} from '@angular/core';
import {ApiService} from '../services/api.service';
import {HttpErrorResponse} from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})

export class HomeComponent implements OnInit {
  model = {
    left: true,
    middle: false,
    right: false
  };

  focus;
  focus1;
  api;

  constructor(api: ApiService) {
    this.api = api
  }

  ngOnInit() {
  }

  uploadDoc(value: string) {
    this.api.uploadImage(value).subscribe(
      (data: any) => {
        console.log(data)
      },
      (error: HttpErrorResponse) => console.error(error), // on error
    );
    console.log(value);
  }
}
