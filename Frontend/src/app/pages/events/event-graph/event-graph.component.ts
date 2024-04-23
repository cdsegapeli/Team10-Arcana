import { HttpClient } from '@angular/common/http';
import { Component, ViewChild } from '@angular/core';
import { DxDiagramComponent } from 'devextreme-angular';
import ArrayStore from 'devextreme/data/array_store';
import { EventsService } from 'src/app/services/events.service';

@Component({
  selector: 'app-event-graph',
  templateUrl: './event-graph.component.html',
  styleUrls: ['./event-graph.component.scss']
})
export class EventGraphComponent {
  @ViewChild(DxDiagramComponent, { static: false }) diagram!: DxDiagramComponent;
  dataSource: any;
  savedDiagram: any;


  constructor(private http: HttpClient, private eventService: EventsService) {
    this.dataSource = ({
      key: 'nodeID',
      data:  this.getEvents() ,
    });
  }


  getEvents(){
    let events
    this.eventService.getSortedEvents().subscribe((result:any)=>{
        console.log(result)
        events = result;
    })
    return events;
  }

  saveEvents(){
    const diagram = this.diagram.instance
    //  $("#diagram").dxDiagram("instance");
     this.savedDiagram = diagram.export()
     console.log(this.savedDiagram,"kill me");
  }
}



