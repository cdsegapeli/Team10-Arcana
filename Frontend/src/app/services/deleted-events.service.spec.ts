import { TestBed } from '@angular/core/testing';

import { DeletedEventsService } from './deleted-events.service';

describe('DeletedEventsService', () => {
  let service: DeletedEventsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DeletedEventsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
