<?php
/**
 * Plugin Name: GCPRO Atomic Masked Image
 * Description: Independently editable photo and SVG mask for Elementor Atomic.
 * Version: 0.4.5
 * Requires Plugins: elementor
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

// Keep WordPress archive bounds on the same nine-item sequence as the grid.
add_action( 'pre_get_posts', static function ( $query ) {
	if ( is_admin() || ! $query->is_main_query() || ! $query->is_post_type_archive( 'gcpro_project' ) ) {
		return;
	}
	$query->set( 'posts_per_page', 9 );
	$query->set( 'orderby', [ 'date' => 'DESC', 'ID' => 'DESC' ] );
} );

// Seed the existing Load More cursor when opening a numbered archive directly.
add_filter( 'wp_grid_builder/facet/query_string', static function ( $params, $grid_id, $action ) {
	if ( 'elementor-element-c61e6a3' === $grid_id && 'render' === $action && empty( $params ) ) {
		$page = max( 1, (int) get_query_var( 'paged' ) );
		$path = wp_parse_url( wp_get_referer() ?: '', PHP_URL_PATH );
		if ( preg_match( '#^/projects/page/([1-9][0-9]*)/$#', (string) $path, $match ) ) {
			$page = (int) $match[1];
		}
		if ( $page > 1 ) {
			$params['gcpro_projects_load_more'] = [ (string) ( ( $page - 1 ) * 9 ) ];
		}
	}
	return $params;
}, 10, 3 );

add_action( 'elementor/widgets/register', static function ( $manager ) {
	if ( ! class_exists( '\Elementor\Modules\AtomicWidgets\Elements\Base\Atomic_Widget_Base' ) ) { return; }
	require_once __DIR__ . '/masked-image.php';
	$manager->register( new \GCPRO\Atomic\Masked_Image() );
	require_once __DIR__ . '/trustindex-badge.php';
	$manager->register( new \GCPRO\Atomic\Trustindex_Badge() );
}, 20 );

// Project labels only: layout and presentation remain native Elementor controls.
add_action( 'elementor/dynamic_tags/register', static function ( $manager ) {
	class GCPRO_Project_Service_Tag extends \Elementor\Core\DynamicTags\Tag {
		public function get_name() { return 'gcpro-project-primary-service'; }
		public function get_title() { return 'Project Primary Service'; }
		public function get_group() { return 'post'; }
		public function get_categories() { return [ 'text' ]; }
		public function render() {
			$id = get_the_ID();
			if ( 'gcpro_project' !== get_post_type( $id ) ) { return; }
			$terms = get_the_terms( $id, 'project_service' );
			if ( empty( $terms ) || is_wp_error( $terms ) ) { return; }
			$selected = null;
			if ( class_exists( '\AIOSEO\Plugin\Common\Models\Post' ) ) {
				$primary = \AIOSEO\Plugin\Common\Models\Post::getPost( $id )->primary_term;
				$primary_id = is_object( $primary ) ? (int) ( $primary->project_service ?? 0 ) : 0;
				foreach ( $terms as $term ) {
					if ( $term->term_id === $primary_id ) { $selected = $term; break; }
				}
			}
			// A sole assignment is unambiguous; never use array order as a primary.
			if ( ! $selected && 1 === count( $terms ) ) { $selected = reset( $terms ); }
			if ( $selected ) { echo esc_html( $selected->name ); }
		}
	}
	class GCPRO_Project_Location_Tag extends \Elementor\Core\DynamicTags\Tag {
		public function get_name() { return 'gcpro-project-location'; }
		public function get_title() { return 'Project Classified Location'; }
		public function get_group() { return 'post'; }
		public function get_categories() { return [ 'text' ]; }
		protected function register_controls() {
			$this->add_control( 'state', [
				'label' => 'Verified state code',
				'type' => \Elementor\Controls_Manager::TEXT,
				'default' => '',
				'description' => 'Use only when every location in this selection is verified in the same state. Leave blank for city only.',
			] );
		}
		public function render() {
			$id = get_the_ID();
			if ( 'gcpro_project' !== get_post_type( $id ) ) { return; }
			$terms = get_the_terms( $id, 'project_area' );
			if ( empty( $terms ) || is_wp_error( $terms ) || 1 !== count( $terms ) ) { return; }
			$term = reset( $terms );
			$state = strtoupper( trim( (string) $this->get_settings( 'state' ) ) );
			$suffix = preg_match( '/^[A-Z]{2}$/', $state ) ? ', ' . $state : '';
			echo esc_html( $term->name . $suffix );
		}
	}
	$manager->register( new GCPRO_Project_Service_Tag() );
	$manager->register( new GCPRO_Project_Location_Tag() );
} );
