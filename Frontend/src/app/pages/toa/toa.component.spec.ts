import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToaComponent } from './toa.component';

describe('ToaComponent', () => {
  let component: ToaComponent;
  let fixture: ComponentFixture<ToaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ToaComponent]
    });
    fixture = TestBed.createComponent(ToaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
