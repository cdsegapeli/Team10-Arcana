import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WebsitecolorComponent } from './websitecolor.component';

describe('WebsitecolorComponent', () => {
  let component: WebsitecolorComponent;
  let fixture: ComponentFixture<WebsitecolorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [WebsitecolorComponent]
    });
    fixture = TestBed.createComponent(WebsitecolorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
