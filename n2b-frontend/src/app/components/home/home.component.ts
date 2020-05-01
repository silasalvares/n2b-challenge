import { Component, OnInit } from '@angular/core';
import { ReviewService } from 'src/app/services/reviews.service';
import { Review } from 'src/app/models/review.model';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

	cols: any[];
	reviews: Review[];
	totalRecords: number = 0;
	filters: Review = new Review();
	appliedFilters: Review = new Review();

	constructor(private reviewService: ReviewService) { }

	ngOnInit() {
		this.cols = [
            { field: 'country', header: 'Country' },
            { field: 'description', header: 'Description' },
            { field: 'points', header: 'Points' },
			{ field: 'price', header: 'Price' },
			{ field: 'variety', header: 'Variety' }
		];
	}

	public search() {
		this.loadReviews(1, this.filters);
	}

	private loadReviews(page: number, filters: Review) {
		this.reviewService.search(page, filters).subscribe(
			apiResponse => {
				this.appliedFilters = this.filters;
				this.reviews = apiResponse['data']['reviews'];
				this.totalRecords = apiResponse['data']['total_records'];
			},
			error => {
				console.log(error);
			}
		);
	}

	public loadPage(event) {
		let page = (event['first']+10)/10;
		console.log(page);
		this.loadReviews(page, this.appliedFilters);
	}

	public clear() {
		this.filters = new Review();
		this.search();
	}

}
