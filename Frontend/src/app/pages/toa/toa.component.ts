import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Toa } from 'src/app/models/toas';
import { ToaService } from 'src/app/services/toa.service';

@Component({
  selector: 'app-toa',
  templateUrl: './toa.component.html',
  styleUrls: ['./toa.component.scss']
})
export class ToaComponent {
  toas: Toa[] = [];
  custToas: Toa[] = [];
  newFile: String = '';

  constructor(private toaService: ToaService, private router: Router){

  }

  ngOnInit(){
    this.toaService.getToas().subscribe((result:any)=>{
      result.forEach((data:any) => {
        let toa: Toa = {
          ID: data['_id'],
          Team: data['team'],
          ActionName: data['actionName'],
          IconFilename: "assets/images/"+data['iconFilename'],
        }
        this.toas.push(toa)
      })
    })
    this.toaService.getCustToas().subscribe((result:any)=>{
      result.forEach((data:any) => {
        let custToa: Toa = {
          ID: data['_id'],
          Team: data['team'],
          ActionName: data['actionName'],
          IconFilename: "assets/images/"+data['iconFilename'],
        }
        this.custToas.push(custToa)
      })
    })
  }

  onAddToa(toa: any){
    toa.data['IconFilename'] = this.newFile
    console.log(toa.data)
    this.toaService.addToa(toa.data)
    setTimeout(()=>{
      window.location.reload()
    }, 500)
  }

  onUpdateToa(toa: any){
    toa.data['IconFilename'] = this.newFile
    this.toaService.updateToa(toa.data)
    setTimeout(()=>{
      window.location.reload()
    }, 500)
  }

  onDeleteToa(toa: any){
    this.toaService.deleteToa(toa.data)
  }

  onAddCustToa(toa: any){
    toa.data['IconFilename'] = this.newFile
    console.log(toa.data)
    this.toaService.addCustToa(toa.data)
    setTimeout(()=>{
      window.location.reload()
    }, 500)
  }

  onUpdateCustToa(toa: any){
    toa.data['IconFilename'] = this.newFile
    this.toaService.updateCustToa(toa.data)
    setTimeout(()=>{
      window.location.reload()
    }, 500)
  }

  onDeleteCustToa(toa: any){
    this.toaService.deleteCustToa(toa.data)
  }

  onValueChanged(file: any){
    console.log(file.value[0]['name'])
    this.newFile = file.value[0]['name']
  }

  goToEvents(){
    this.router.navigateByUrl('/event')
  }

}
