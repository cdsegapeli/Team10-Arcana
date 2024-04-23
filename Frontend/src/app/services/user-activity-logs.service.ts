import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment.development';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserActivityLogsService {

  constructor(private http:HttpClient) { }

  getUserActivityLogs():Observable<any>{
    return this.http.get(environment.apiUrl+"/view-user-activity-logs");
  }
}
