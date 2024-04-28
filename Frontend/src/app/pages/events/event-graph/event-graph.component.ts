import { HttpClient } from '@angular/common/http';
import { Component, OnInit, ViewChild } from '@angular/core';
import { DxDiagramComponent } from 'devextreme-angular';
import ArrayStore from 'devextreme/data/array_store';
import { EventsService } from 'src/app/services/events.service';
import { Event } from 'src/app/models/events';

@Component({
  selector: 'app-event-graph',
  templateUrl: './event-graph.component.html',
  styleUrls: ['./event-graph.component.scss']
})
export class EventGraphComponent implements OnInit{
  @ViewChild(DxDiagramComponent, { static: false }) diagram!: DxDiagramComponent;
  dataSource!: ArrayStore;
  savedDiagram: any;
  events: Event[] = [];
  currentEvent: Event = new Event;
  popupVisible = false;


  constructor(private http: HttpClient, private eventService: EventsService) {

  }
  ngOnInit(){
    this.getEvents();
  }

  getEvents(){
    this.eventService.getSortedEvents().subscribe((result:any)=>{
        console.log(result)
        this.dataSource = new ArrayStore({
          key: 'ID',
          data:  result,
        });
        // result.forEach((data:any) => {
        //   let event: Event = {
        //     ID: data['_id'],
        //     Date: data['date'],
        //     Time: data['time'],
        //     VectorID: data['vectorID'],
        //     Description: data['description'],
        //     Analyst: data['analyst'],
        //     Team: data['team'],
        //     Posture: data['posture'],
        //     SourceIP: data['sourceIP'],
        //     TargetIP: data['targetIP'],
        //     Location: data['location'],
        //     LastModifiedDate: data['lastModifiedDate'],
        //     LastModifiedTime: data['lastModifiedTime']
        //   }
        //   this.events.push(event)
        // })
    })
  }

  showInfo(event: any){
    this.currentEvent = event
    this.popupVisible = true
  }

  saveEvents(){
    const diagram = this.diagram.instance
    //  $("#diagram").dxDiagram("instance");
     this.savedDiagram = diagram.export()
     this.eventService.saveGraph(this.savedDiagram)
     console.log(this.savedDiagram,"kill me");
  }

  itemTypeExpr(obj: any, value: any) {
    return obj.Type === 'diamond'; 

  }
}



