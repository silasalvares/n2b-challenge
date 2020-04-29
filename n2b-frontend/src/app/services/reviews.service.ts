import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
	providedIn: 'root'
})
export class ReviewService {

	constructor(private http: HttpClient) { }

	public search() {
		return this.http.post(environment.apiUrl + '/search/', {'page': 1, "filter_data": {}});
	}
}
