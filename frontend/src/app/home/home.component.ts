import {Component, OnInit} from '@angular/core';
import {ApiService} from '../services/api.service';
import {HttpErrorResponse} from '@angular/common/http';
import {Router} from "@angular/router"
import {SharedService} from "../services/shared.service"

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
  api: ApiService;
  shared: SharedService;

  constructor(api: ApiService, private router: Router, private shared: SharedService) {
    this.api = api
    this.shared = shared
  }

  ngOnInit() {
  }

  uploadDoc(value: string) {
    this.shared.setFileData(value)
    this.api.uploadImage(value).subscribe(
      (data: any) => {
        console.log(data)
//         this.shared.setFileData(data)
//         console.log("yoyo"+this.shared.getFileData())
        this.router.navigate(['/claim-form'])
      },
      (error: HttpErrorResponse) => this.router.navigate(['/claim-form']), // on error
    );
    console.log(value);
  }
}
