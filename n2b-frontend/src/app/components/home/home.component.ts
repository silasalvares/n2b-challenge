import { Component, OnInit } from '@angular/core';
import { ReviewService } from 'src/app/services/reviews.service';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

	cols: any[];
	reviews: any[];

	constructor(private reviewService: ReviewService) { }

	ngOnInit() {
		this.cols = [
            { field: 'country', header: 'Country' },
            { field: 'description', header: 'Description' },
            { field: 'points', header: 'Points' },
			{ field: 'price', header: 'Price' },
			{ field: 'variety', header: 'Variety' }
		];
		
		this.loadReviews();
	}

	private loadReviews() {
		this.reviewService.search().subscribe(
			apiResponse => {
				console.log(apiResponse);
				this.reviews = apiResponse['data'];
			},
			error => {
				console.log(error);
			}
		);
	}

	

}
