import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { EventsComponent } from './pages/events/events.component';
import { ProjectComponent } from './pages/project/project.component';
import { EventFormComponent } from './components/event-form/event-form.component';
import { SyncComponent } from './pages/sync/sync.component';
import { WebsitecolorComponent } from './pages/websitecolor/websitecolor.component';
import { HeaderComponent } from './components/header/header.component';
import { EventGraphComponent } from './pages/events/event-graph/event-graph.component';
import { DxDiagramModule, DxDiagramComponent } from 'devextreme-angular';
import { DxDataGridModule, DxFileUploaderModule, DxButtonModule, DxPopupModule, DxFormModule, DxTextAreaModule, DxDateBoxModule } from 'devextreme-angular';
import { FormsModule } from '@angular/forms';
import { ToaComponent } from './pages/toa/toa.component';
import { DeletedEventsComponent } from './pages/deleted-events/deleted-events.component';
import { UserActivityLogsComponent } from './pages/user-activity-logs/user-activity-logs.component';




@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    EventsComponent,
    ProjectComponent,
    EventFormComponent,
    SyncComponent,
    WebsitecolorComponent,
    HeaderComponent,
    EventGraphComponent,
    ToaComponent,
    DeletedEventsComponent,
    UserActivityLogsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    DxDataGridModule,
    HttpClientModule,
    DxDiagramModule,
    DxFileUploaderModule,
    DxButtonModule,
    DxPopupModule,
    FormsModule,
    HttpClientModule, 
    DxFormModule,
    DxDateBoxModule,
    DxTextAreaModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
