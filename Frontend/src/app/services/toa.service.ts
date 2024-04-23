import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Toa } from '../models/toas';

@Injectable({
  providedIn: 'root'
})
export class ToaService {

  constructor(private http:HttpClient) { 

  }

  getToas():Observable<any>{
    return this.http.get(environment.apiUrl+"/view-toas");
  }

  getCustToas():Observable<any>{
    return this.http.get(environment.apiUrl+"/view-custom-toas");
  }

  addToa(toa: Toa){
    console.log(toa['IconFilename'])
    this.http.post(environment.apiUrl+"/create-base-toa", toa).subscribe()
  }

  addCustToa(toa: Toa){
    this.http.post(environment.apiUrl+"/create-custom-toa", toa).subscribe()
  }

  updateToa(toa: Toa){
    this.http.post(environment.apiUrl+"/update-base-toa", toa).subscribe()
  }

  updateCustToa(toa: Toa){
    this.http.post(environment.apiUrl+"/update-custom-toa", toa).subscribe()
  }

  deleteToa(toa: Toa){
    this.http.post(environment.apiUrl+"/delete-base-toa", toa).subscribe()
  }

  deleteCustToa(toa: Toa){
    this.http.post(environment.apiUrl+"/delete-custom-toa", toa).subscribe()
  }
}
