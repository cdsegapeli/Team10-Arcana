import { Component } from '@angular/core';
import { Renderer2, ElementRef, ViewChild } from '@angular/core';
import { ColorSchemeService } from '../../color-scheme.service';

@Component({
  selector: 'app-websitecolor',
  templateUrl: './websitecolor.component.html',
  styleUrls: ['./websitecolor.component.scss']
})
export class WebsitecolorComponent {
  selectedColorScheme = 'default';

 

  constructor(private renderer: Renderer2, private colorSchemeService: ColorSchemeService) {}

  saveColorScheme(scheme: string) {
    this.colorSchemeService.changeColorScheme(scheme);
  }


}
