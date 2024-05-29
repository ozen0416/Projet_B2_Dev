<?php
class Database
{
  private $dbh;

  function __construct()
  {
    $this->dbh = Connection::Connect();
  }

  function create($table, $params)
  {
    // Format keys and values to fit the SQL command
    $keys = Format::ArrRefactor(array_keys($params));
    $values = Format::ArrRefactor(array_keys($params));

    $cmd = "INSERT INTO `$table` ($keys) VALUES ($values)";

    $sth = $this->dbh->prepare($cmd);

    foreach ($params as $key => $value) {
      // TODO error handling
      $sth->bindValue($key, $value);
    }

    try {
      $sth->execute();
      return json_encode(['Success' => 'Command went through']);
    } catch (\PDOException $e) {
      return json_encode(['Error' => $e->getMessage()]);
    }
  }

  function read($table, $columns, $whereCondition = array())
  {

    if ($columns != "*") {
      //Get string of keys from params array
      $col = Format::ArrRefactor($columns);
    } else {
      $col = "*";
    }

    // Build command with or without a filter
    $cmd = "SELECT $col FROM `$table`";
    if (!empty($whereCondition)) {
      try {
        $cmd .= "(" . $this->buildWhereCondition($whereCondition) . ")";
      } catch (\Exception $e) {
        return json_encode(['Error' => $e->getMessage()]);
      }
    }

    $sth = $this->dbh->prepare($cmd);
    foreach ($whereCondition as $key => $value) {
      $sth->bindParam($key, $value["value"]);
    }
    try {
      $sth->execute();
      return json_encode($sth->fetchAll(\PDO::FETCH_ASSOC));
    } catch (\PDOException $e) {
      return json_encode(['Error' => $e->getMessage()]);
    }
  }
  function update($table, $params, $whereCondition)
  {
    // build command
    $cmd = "UPDATE `$table` SET " . $this->buildSetClause($params);
    try {
      $cmd .= " WHERE (" . $this->buildWhereCondition($whereCondition) . ")";
    } catch (\Exception $e) {
      return json_encode(['Error' => $e->getMessage()]);
    }

    $sth = $this->dbh->prepare($cmd);
    // Binding parameters for the SET clause
    foreach ($params as $column => $value) {
      $sth->bindValue(":$column", $value);
    }

    // Binding parameters for the WHERE clause
    foreach ($whereCondition as $column => $condition) {
      $sth->bindValue(":$column", $condition['value']);
    }

    try {
      $sth->execute();
      return json_encode(['Success' => 'Command went through']);
    } catch (\PDOException $e) {
      return json_encode(['Error' => $e->getMessage()]);
    }
  }
  function delete($table, $whereCondition)
  {
    // Build command
    $cmd = "DELETE FROM `$table` WHERE";
    try {
      $cmd .= $this->buildWhereCondition($whereCondition);
    } catch (\Exception $e) {
      return json_encode(['Error' => $e->getMessage()]);
    }


    $sth = $this->dbh->prepare($cmd);
    foreach ($whereCondition as $key => $value) {
      $sth->bindParam($key, $value["value"]);
    }

    try {
      $sth->execute();
      return json_encode(['Success' => 'Command went through']);
    } catch (\PDOException $e) {
      return json_encode(['Error' => $e->getMessage()]);
    }
  }

  private function buildSetClause($updateData)
  {
    $setDataStrings = array();

    foreach ($updateData as $column => $value) {
      $setDataStrings[] = "$column = :$column";
    }

    return Format::ArrRefactor($setDataStrings, "", "%s, ", "");
  }

  function buildWhereCondition($conditions)
  {
    // TODO error handling
    //  $column in foreach is not sanitized
    $conditionStrings = array();

    $allowedOperators = ['=', '<', '>', '<=', '>=', '<>', '!='];

    foreach ($conditions as $column => $condition) {
      // Ensure that the condition array has both 'operator' and 'value'
      if (isset($condition['operator']) && isset($condition['value'])) {
        $operator = $condition["operator"];
        // Check if the operator is in the whitelist
        if (in_array($operator, $allowedOperators)) {
          // Concatenate the condition string only if the operator is valid
          $conditionStrings[] = "$column $operator :$column";
        } else {
          throw new \Exception('Wrong operator was sent');
        }
      } else {
        throw new \Exception('Invalid keys from JSON were sent');
      }
    }
    return Format::ArrRefactor($conditionStrings, "WHERE", " %s AND");
  }
}
