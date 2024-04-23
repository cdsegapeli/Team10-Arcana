import { Injectable } from '@angular/core';
import { Project } from '../models/projects';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class ProjectsService {

  constructor(private http:HttpClient) { 

  }
  getProjects():Observable<any>{
    return this.http.get(environment.apiUrl+"/view-projects");
  }

  openProject(project: Project){
    this.http.post(environment.apiUrl+"/open-project", project).subscribe()
  }
  
  updateProject(project: Project){
    this.http.post(environment.apiUrl+"/update-project",project).subscribe()
  }

  addProject(project: Project){
    this.http.post(environment.apiUrl+"/create-project", project).subscribe()
  }

  deleteProject(project: Project){
    this.http.post(environment.apiUrl+"/delete-project", project).subscribe()
  }
}
