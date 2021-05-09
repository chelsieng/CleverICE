import {Component, OnInit} from '@angular/core';
import {SharedService} from '../services/shared.service'
import {ApiService} from "../services/api.service";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})

export class ProfileComponent implements OnInit {
  focus;
  focus1;
  shared: SharedService;
  name;
  phoneNum;
  policyNum;
  email;
  situation;
  location;
  amount;
  summary;
  api;
  response;

  constructor(api: ApiService, shared: SharedService) {
    this.shared = shared
    this.api = api
  }

  ngOnInit() {
    this.api.scanFilename(this.shared.getFileData()).subscribe(
      (data: string) => {console.log(data)}
    );
//     ,
//       (error: HttpErrorResponse) => this.response), // on error
//     );
  }

}
