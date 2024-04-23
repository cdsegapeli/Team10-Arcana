import { TestBed } from '@angular/core/testing';

import { ToaService } from './toa.service';

describe('ToaService', () => {
  let service: ToaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ToaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
