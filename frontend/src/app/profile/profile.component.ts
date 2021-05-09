import {Component, OnInit} from '@angular/core';
import {SharedService} from '../services/shared.service'
import {ApiService} from "../services/api.service";
import {ClaimInfo} from "../models/claim-info.model";
import {HttpErrorResponse} from '@angular/common/http';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})

export class ProfileComponent implements OnInit {
  focus;
  focus1;
  shared: SharedService;
  api;
  claim: ClaimInfo;

  constructor(api: ApiService, shared: SharedService) {
    this.shared = shared
    this.api = api
  }

  ngOnInit() {
    this.api.scanFilename(this.shared.getFileData()).subscribe(
      (data: any) => {
        data[0] = this.claim.name;
        data[1] = this.claim.phoneNum;
        data[2] = this.claim.policyNum;
        data[3] = this.claim.email;
        data[4] = this.claim.situation;
        data[5] = this.claim.location;
        data[6] = this.claim.amount;
        data[7] = this.claim.summary;
      },
      (error: HttpErrorResponse) => console.log(error)// on error
    );
  }

}
