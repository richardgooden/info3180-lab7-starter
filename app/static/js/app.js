// Your JavaScript Code here
const app = angular.module('MyApp', []);

app.controller('MyCtrl', function($scope, $http) {
  $scope.thumbs = [];
  $http.get('/api/thumbnails')
    .then(function(response) {
         let a = response.data;
         $scope.thumbs = a.thumbnails;
         
    });
    
})