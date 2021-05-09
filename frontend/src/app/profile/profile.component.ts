import {Component, OnInit} from '@angular/core';
import {SharedService} from '../services/shared.service'

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})

export class ProfileComponent implements OnInit {
  focus;
  focus1;
  shared: SharedService;

  constructor(private shared: SharedService) {
    this.shared = shared
  }

  ngOnInit() {
    console.log(this.shared.getFileData())
  }

}
