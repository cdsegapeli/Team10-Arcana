import { Injectable } from '@angular/core';

export class Event {
    ID!: String; 
    Date!: Date;
    Time!: Date;
    VectorID!: String;
    Description!: String;
    Analyst!: String;
    Team!: String;
    Posture!: String;
    SourceIP!: String;
    TargetIP!: String;
    Location!: String;
    LastModifiedDate!: Date;
    LastModifiedTime!: Date;
  
  }

  @Injectable()
  export class Service {

  }