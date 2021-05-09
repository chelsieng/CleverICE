import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  fileData: String
  fileName: String
  constructor() { }

  setFileData(file): void{
    this.fileData = file
  }

  setFileName(file): void{
    this.fileName = file
  }

  getFileData(): String{
    return this.fileData
  }

  getFileName(): String{
    return this.fileName
  }

}
