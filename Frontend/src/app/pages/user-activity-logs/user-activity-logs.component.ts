import { Component } from '@angular/core';
import { UserActivityLog } from 'src/app/models/userActvityLog';
import { UserActivityLogsService } from 'src/app/services/user-activity-logs.service';

@Component({
  selector: 'app-user-activity-logs',
  templateUrl: './user-activity-logs.component.html',
  styleUrls: ['./user-activity-logs.component.scss']
})
export class UserActivityLogsComponent {
  logs: UserActivityLog [] = [];

  constructor(private userActivityService: UserActivityLogsService){ }

  ngOnInit(){
    this.userActivityService.getUserActivityLogs().subscribe((result:any)=>{
      result.forEach((data:any) => {
        let log: UserActivityLog = {
          ID: data['_id'],
          Log: data['activity'],
          Timestamp: data['timestamp'],
        }
        this.logs.push(log)
      })
    })
  }
}
