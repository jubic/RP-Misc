<?php
class Products_model extends CI_Model {
	
	function get_all() {
		
		$results = $this->db->get('products')->result();
		
		foreach ($results as $result) {
			
			if ($result->option_value) {
				$result->option_value = explode(',',$result->option_value);
			}
			
		}
		
		return $results;
		
	}
	
	function get($id) {
		
		$results = $this->db->get_where('products', array('id' => $id))->result();
		$result = $results[0];
		
		if ($result->option_value) {
			$result->option_value = explode(',',$result->option_value);
		}
		
		return $result;
	}
	
}
?>