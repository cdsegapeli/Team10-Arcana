import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';


@Injectable({
  providedIn: 'root',
})
export class ColorSchemeService {
  
  private colorScheme = new BehaviorSubject<string>('header-default'); // default class
  currentColorScheme = this.colorScheme.asObservable();

  constructor() {}

  changeColorScheme(scheme: string) {
    this.colorScheme.next('header-' + scheme);
  }
}
