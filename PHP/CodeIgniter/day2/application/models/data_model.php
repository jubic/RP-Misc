<?php

class Data_model extends CI_Model {

    // Query
    /* function getAll() {

      $q = $this->db->query("SELECT * FROM `data`");

      if ($q->num_rows() > 0) {
      foreach ($q->result() as $row) {
      $data[] = $row;
      }
      return $data;
      }
      } */

    // Active Records
    /* function getAll() {

      $q = $this->db->get('data');

      if ($q->num_rows() > 0) {
      foreach ($q->result() as $row) {
      $data[] = $row;
      }
      return $data;
      }
      }
     */

    // Specific Query
    /* function getAll() {

      $this->db->select('title, contents');
      $q = $this->db->get('data');

      if ($q->num_rows() > 0) {
      foreach ($q->result() as $row) {
      $data[] = $row;
      }
      return $data;
      }
      }
     */

    // Query Finding
    /* function getAll() {

      $sql = "SELECT title, author, contents FROM data where id = ? AND author = ?";
      $q = $this->db->query($sql, array(2, 'Jubic'));

      if ($q->num_rows() > 0) {
      foreach ($q->result() as $row) {
      $data[] = $row;
      }
      return $data;
      }
      }
     */

    // Specific Active Record
    function getAll() {
        $this->db->select('title, contents');
        $this->db->from('data');
        $this->db->where('id', 2);


        $q = $this->db->get();

        if ($q->num_rows() > 0) {
            foreach ($q->result() as $row) {
                $data[] = $row;
            }
            return $data;
        }
    }

}

?>