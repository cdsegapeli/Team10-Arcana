import { Injectable } from '@angular/core';
import { Event } from '../models/events';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class DeletedEventsService {

  constructor(private http:HttpClient) { }

  getDeletedEvents():Observable<any>{
    return this.http.get(environment.apiUrl+"/view-deleted-events");
  }

  recoverEvent(event: Event){
    this.http.post(environment.apiUrl+"/recover-event", event).subscribe()
  }
}
