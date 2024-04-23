import { Component, OnDestroy } from '@angular/core';
import { ColorSchemeService } from '../../color-scheme.service'; // correct path to your service
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnDestroy {
  colorSchemeSubscription: Subscription;
  currentSchemeClass = 'header-default';

  constructor(private colorSchemeService: ColorSchemeService) {
    this.colorSchemeSubscription = this.colorSchemeService.currentColorScheme.subscribe(scheme => {
      console.log("Received color scheme class: ", scheme);
      this.currentSchemeClass = scheme;
    });
  }

  ngOnDestroy() {
    this.colorSchemeSubscription.unsubscribe();
  }
}