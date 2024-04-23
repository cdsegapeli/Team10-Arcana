import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeletedEventsComponent } from './deleted-events.component';

describe('DeletedEventsComponent', () => {
  let component: DeletedEventsComponent;
  let fixture: ComponentFixture<DeletedEventsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DeletedEventsComponent]
    });
    fixture = TestBed.createComponent(DeletedEventsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
