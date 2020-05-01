import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Review } from '../models/review.model';

@Injectable({
	providedIn: 'root'
})
export class ReviewService {

	constructor(private http: HttpClient) { }

	public search(page: number, filters: Review) {
		return this.http.post(environment.apiUrl + '/search/', {'page': page, "filter_data": filters});
	}
}
