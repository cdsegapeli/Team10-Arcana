import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Event } from 'src/app/models/events';
import { DeletedEventsService } from 'src/app/services/deleted-events.service';

@Component({
  selector: 'app-deleted-events',
  templateUrl: './deleted-events.component.html',
  styleUrls: ['./deleted-events.component.scss']
})
export class DeletedEventsComponent {
  event: Array<string> = [];
  deletedEvents: Event[] = [];

  constructor(private deletedEventService: DeletedEventsService, private router: Router){

  }

  ngOnInit(){
    this.deletedEventService.getDeletedEvents().subscribe((result:any)=>{
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
        this.deletedEvents.push(event)
      })
    })
  }

  onRecoverEvent(event: any){
    console.log(event.data)
    this.deletedEventService.recoverEvent(event.data)
  }

  goToEvents(){
    this.router.navigateByUrl('/event')
  }

  logEvent(eventName: string) {
    this.event.unshift(eventName);
    console.log(eventName)
  }

  onRowInserting(project: any){
    console.log("this is project",project.data)
    
  }
}
