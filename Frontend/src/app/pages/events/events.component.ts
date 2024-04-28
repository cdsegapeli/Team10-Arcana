import { Component } from '@angular/core';
import { Event } from 'src/app/models/events';
import { EventsService } from 'src/app/services/events.service';
import { RouterModule, Router } from '@angular/router';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.scss']
})
export class EventsComponent {
  event: Array<string> = [];
  events: Event[] = [];
  fileUrl: any;
  isPopupVisible: boolean;

  constructor(private eventService: EventsService, private router: Router, private sanitizer: DomSanitizer){
    this.isPopupVisible = false
  }

  ngOnInit(){
    this.eventService.getEvents().subscribe((result:any)=>{
      result.forEach((data:any) => {
        let event: Event = {
          ID: data['_id'],
          Date: data['date'],
          Time: data['time'],
          VectorID: data['vectorID'],
          Description: data['description'],
          Analyst: data['analyst'],
          Team: data['team'],
          Posture: data['posture'],
          SourceIP: data['sourceIP'],
          TargetIP: data['targetIP'],
          Location: data['location'],
          LastModifiedDate: data['lastModifiedDate'],
          LastModifiedTime: data['lastModifiedTime']
        }
        this.events.push(event)
      })
    })
    this.eventService.exportProject().subscribe(
      (result:any)=>{ 
        const data = JSON.stringify(result)
        console.log(result)
        const blob = new Blob([data], { type: 'application/octet-stream' })
        this.fileUrl = this.sanitizer.bypassSecurityTrustResourceUrl(window.URL.createObjectURL(blob));
      })
  }

  onAddEvent(newEvent: any){
    console.log(newEvent.data)
    this.eventService.addEvent(newEvent.data)
    setTimeout(()=>{
      window.location.reload()
    }, 100)
  }

  onUpdateEvent(newEvent: any){
    console.log(newEvent.data)
    this.eventService.updateEvent(newEvent.data)
  }

  onEventDelete(event: any){
    console.log(event.data)
    this.eventService.deleteEvent(event.data)
  }

  logEvent(eventName: string) {
    this.event.unshift(eventName);
    console.log(eventName)
  }

  onRowInserting(project: any){
    console.log("this is project",project.data)
    
  }

  goToDeletedEvents(){
    this.router.navigateByUrl('/deleted-events')
  }

  goToGraph(){
    // TODO: fix route to graph page
    this.router.navigateByUrl('/graph')
  }

  goToTOA(){
    this.router.navigateByUrl('/toa')
  }

  exportProject(){
    this.eventService.exportProject().subscribe(
      (result:any)=>{ 
        const data = result.data
        const blob = new Blob([data], { type: 'application/octet-stream' })
        this.fileUrl = this.sanitizer.bypassSecurityTrustResourceUrl(window.URL.createObjectURL(blob));
      })
  }

  togglePopup(){
    this.isPopupVisible = !this.isPopupVisible
    console.log(this.isPopupVisible)
  }
}
