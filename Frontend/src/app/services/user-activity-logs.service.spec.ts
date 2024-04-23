import { TestBed } from '@angular/core/testing';

import { UserActivityLogsService } from './user-activity-logs.service';

describe('UserActivityLogsService', () => {
  let service: UserActivityLogsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UserActivityLogsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
