import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { EventsComponent } from './pages/events/events.component';
import { ProjectComponent } from './pages/project/project.component';
import { EventFormComponent } from './components/event-form/event-form.component';
import { SyncComponent } from './pages/sync/sync.component';
import { WebsitecolorComponent } from './pages/websitecolor/websitecolor.component';
import { RequestComponent } from './pages/sync/request/request.component';
import { LogsComponent } from './components/logs/logs.component';
import { EventGraphComponent } from './pages/events/event-graph/event-graph.component';
import { ToaComponent } from './pages/toa/toa.component';
import { DeletedEventsComponent } from './pages/deleted-events/deleted-events.component';
import { UserActivityLogsComponent } from './pages/user-activity-logs/user-activity-logs.component';

const routes: Routes = [
  { path:  '', component: ProjectComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'event', component: EventsComponent },
  { path: 'project', component: ProjectComponent },
  { path: 'eventForm', component: EventFormComponent },
  { path: 'sync', component: SyncComponent },
  { path: 'log', component: LogsComponent },
  { path: 'webcolor', component: WebsitecolorComponent },
  { path: 'sync/request', component: RequestComponent },
  { path: 'manage/projects', component: ProjectComponent},
  { path: 'event/graph', component: EventGraphComponent},
  { path: 'toa', component: ToaComponent},
  { path: 'deleted-events', component: DeletedEventsComponent},
  { path: 'user-activity-logs', component: UserActivityLogsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
