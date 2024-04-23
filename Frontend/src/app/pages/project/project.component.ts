import { Component } from '@angular/core';
import { RouterModule, Router } from '@angular/router';
import { Project } from 'src/app/models/projects';
import { ProjectsService } from 'src/app/services/projects.service';

@Component({
  selector: 'app-project',
  templateUrl: './project.component.html',
  styleUrls: ['./project.component.scss']
})
export class ProjectComponent {
  events: Array<string> = [];
  projects: Project[] = [];

  constructor(private projectService: ProjectsService, private router: Router) {

  }
  ngOnInit() {
    this.projectService.getProjects().subscribe((result:any)=>{
    result.forEach((data:any) => {
      let project: Project = {
        ID: data['_id'],
        Name: data['name'],
        Analyst: data['analyst'],
        EndDate: data['endDate'],
        StartDate: data['startDate'],
        StartTime: data['startTime'],
        EndTime: data['endTime'],
      }
      this.projects.push(project)
    });
  })
  }

  onOpenProject(project: any){
    this.projectService.openProject(project.data)
    console.log(project.data)
    this.router.navigateByUrl('/event')
  }

  onAddProject(newProject: any){
    console.log(newProject.data)
    this.projectService.addProject(newProject.data)
    setTimeout(()=>{
      window.location.reload()
    }, 500)
  }

  onUpdateProject(newProject: any){
    console.log(newProject.data)
    this.projectService.updateProject(newProject.data)
  }

  onProjectDelete(project: any){
    console.log(project.data)
    this.projectService.deleteProject(project.data)
  }

  logEvent(eventName: string) {
    this.events.unshift(eventName);
    console.log(eventName)
  }

  onRowInserting(project: any){
    console.log("this is project",project.data)
    
  }

  onValueChanged(file: any){
    console.log(file.value[0]['name'])
    this.uploadDocument(file)
 
  }

  uploadDocument(file: File) {
    let fileReader = new FileReader();
    fileReader.onload = (e) => {
      console.log(fileReader.result);
    }
    console.log(fileReader.readAsText(file));
  }

  refreshPage(){
    window.location.reload()
  }
}
