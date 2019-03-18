import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import {Heroes} from '../mock-hero';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css']
})

export class HeroesComponent implements OnInit {
  hero: Hero = {
    id: 1,
    name: 'Windstorm'
  };

  states = ['Andaman and Nicobar Islands', 'Andhra Pradesh',
  'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
  'Chhattisgarh', 'Dadra and Nagar Haveli', 'Goa', 'Gujarat',
  'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir ', 'Jharkhand',
  'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
  'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
  'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana ',
  'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
];
districts = ['Hyderabad', 'Kutch'];

crops = ['Rice', 'grain', 'wheat'];
seasons = ['Summer', 'Winter', 'Autumn', 'Whole Year'];
years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012];


  stateSelected: any;
  districtSelected: any;
  cropSelected: any;
  yearSelected: any;
  seasonSelected: any;
  areaSelected: any;
  data = 'xyz'
  result: any;

  state: any;
  district: any;
  crop: any;
  season: any;
  area: any;
  year: any;

  constructor(private http:HttpClient) {

   }

  ngOnInit() {

  }
  predict(){
    //postHttpRequest(){
      //var data = {"dummy": 123};
      console.log("in this.predict()");
      var data = {"state": this.state, "district": this.district, "year": this.year,"crop": this.crop, "season": this.season,"area": this.area}
      this.http.post('http://127.0.0.1:8030/postrequest', data).subscribe(
        res => {
          console.log("answer")
          this.result = res.toString();
          console.log(this.result);
        }
      )
    //}
  }



  onStateSelected(event){
    console.log(event); //option value will be sent as event
    this.state = event;
  }

   onDistrictSelected(event){
    console.log(event); //option value will be sent as event
    this.district =  event;
   }

   onCropSelected(event){
    console.log(event); //option value will be sent as event
    this.crop = event;
   }

   onSeasonSelected(event){
    console.log(event); //option value will be sent as event
    this.season = event;
   }

   onYearSelected(event) {
    console.log(event); //option value will be sent as event
     this.year=event;
   }

   onAreaSelected(event) {
    console.log(event.srcElement.value); //option value will be sent as event
    this.area = event.srcElement.value;
   }
}
