angular
  .module("AccountListApp", [])
  .controller("AccountListController", function($scope, $http) {
    $scope.list = [];

    $scope.addNewAccount = () => {
      // Testing the add function (modify later)
      newItem = {
        $$hashKey: "object:17",
        id: 20,
        name: "Testing Angular",
        account_type: "CA",
        bank_name: "NU",
        card_name: "In SQL",
        initial_balance: "123",
        balance: "123",
        user: 1,
        cardImage: "nuCard.png"
      };

      $scope.list.push(newItem);
    };

    let url = "/api/account_list/";

    $http({
      method: "GET",
      url: url
    }).then(response => {
      let data = response.data;

      for (let item of data) {
        item.cardImage = getCardImg(item);
        $scope.list.push(item);
      }
    });
  });
