// Dashboard 1 Morris-chart
$( function () {
	"use strict";


	// Extra chart
	Morris.Area( {
		element: 'extra-area-chart',
		data: [ {
				period: '2001',
				EC2: 0,
				QuickSight: 0,
				Lambda: 90,
				S3: 0,
				RDS: 0
        }, {
				period: '2002',
				EC2: 10,
				QuickSight: 60,
				Lambda: 40,
				S3: 80,
				RDS: 120
        }, {
				period: '2003',
				EC2: 120,
				QuickSight: 10,
				Lambda: 90,
				S3: 30,
				RDS: 50
        }, {
				period: '2004',
				EC2: 0,
				QuickSight: 0,
		        Lambda: 120,
				S3: 0,
				RDS: 0
        }, {
				period: '2005',
				EC2: 0,
				QuickSight: 0,
				Lambda: 0,
				S3: 150,
				RDS: 0
        }, {
				period: '2006',
				EC2: 160,
				QuickSight: 75,
				Lambda: 30,
				S3: 60,
				RDS: 90
        }, {
				period: '2007',
				EC2: 10,
				QuickSight: 120,
				Lambda: 40,
				S3: 60,
				RDS: 30
        }


        ],
		lineColors: [ '#26DAD2', '#fc6180', '#62d1f3', '#ffb64d', '#4680ff' ],
		xkey: 'period',
		ykeys: [ 'EC2', 'QuickSight', 'Lambda', 'S3', 'RDS' ],
		labels: [ 'EC2', 'QuickSight', 'Lambda', 'S3', 'RDS' ],
		pointSize: 0,
		lineWidth: 0,
		resize: true,
		fillOpacity: 0.8,
		behaveLikeLine: true,
		gridLineColor: '#e0e0e0',
		hideHover: 'auto'

	} );



} );
