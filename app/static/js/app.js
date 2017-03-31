// Your JavaScript Code here
const app = angular.module('thumbnailsApp', []);

app.controller('thumbnailsCtrl', function($scope, $http) {
  $scope.thumbnails = [];
  $http.get('/api/thumbnails')
    .then(function(response) {
         let a = response.data;
         $scope.thumbnails = a.thumbnails;
    });
    
})