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
  api

  constructor(api: ApiService, shared: SharedService) {
    this.shared = shared
  }

  ngOnInit() {
    this.api.getScan(this.shared.getFileData()).subscribe(
      (data: any) => {console.log(data)}
    );
  }

}
