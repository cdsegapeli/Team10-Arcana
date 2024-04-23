import { Injectable } from '@angular/core';

export class Project {
  ID!: String; 
  Name!: String;
  Analyst!: String;
  EndDate!: Date;
  EndTime!: Date;
  StartDate!: Date;
  StartTime!: Date;
}

// const projects: Project[] = [{
//     ID: 1,
//     Name: 'project1',
    
//   }, {
//     ID: 2,
//     Name: 'project2',
//   }, {
//     ID: 3,
//     Name: 'project3',
//   }, {
//     ID: 4,
//     Name: 'project4',
//   }, {
//     ID: 5,
//     Name: 'project5',
//   }];
  
  @Injectable()
  export class Service {
    // getProjects(): Project[] {
    //   // return projects;
    // }
  }
  