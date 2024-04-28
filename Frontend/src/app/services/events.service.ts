import { Injectable } from '@angular/core';
import { Event } from '../models/events';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class EventsService {
  constructor(private http:HttpClient) { 

  }

  getEvents():Observable<any>{
    return this.http.get(environment.apiUrl+"/view-events");
  }

  updateEvent(event: Event){
    this.http.post(environment.apiUrl+"/update-event",event).subscribe()
  }

  addEvent(event: Event){
    this.http.post(environment.apiUrl+"/create-event", event).subscribe()
  }

  deleteEvent(event: Event){
    this.http.post(environment.apiUrl+"/delete-event", event).subscribe()
  }

  exportProject(){
    return this.http.get(environment.apiUrl+"/export-project")
  }

  getSortedEvents(): Observable<any> {
    return this.http.get(environment.apiUrl+"/get-sorted-events");
  }

  saveGraph(graph: any){
    this.http.post(environment.apiUrl+"/save-graph", graph).subscribe()
  }
}
