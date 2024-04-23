import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UserActivityLogsComponent } from './user-activity-logs.component';

describe('UserActivityLogsComponent', () => {
  let component: UserActivityLogsComponent;
  let fixture: ComponentFixture<UserActivityLogsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UserActivityLogsComponent]
    });
    fixture = TestBed.createComponent(UserActivityLogsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
