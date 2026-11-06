<?php
/**
 * Plugin Name: GCPRO Atomic Masked Image
 * Description: Independently editable photo and SVG mask for Elementor Atomic.
 * Version: 0.4.7
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


// Keep WPGB's native button and AJAX behavior; reuse the site's existing button class.
add_filter( 'wp_grid_builder/facet/html', static function ( $html ) {
	$tags = new WP_HTML_Tag_Processor( $html );
	while ( $tags->next_tag( [ 'tag_name' => 'BUTTON', 'class_name' => 'wpgb-load-more' ] ) ) {
		$tags->add_class( 'button-outline' );
	}
	return $tags->get_updated_html();
} );

// Render the current shared class through Elementor, without a copied button stylesheet.
add_action( 'wp_enqueue_scripts', static function () {
	if ( is_admin() ) {
		return;
	}
	$repository = '\Elementor\Modules\GlobalClasses\Global_Classes_Repository';
	$renderer = '\Elementor\Modules\AtomicWidgets\Styles\Styles_Renderer';
	if ( ! class_exists( $repository ) || ! class_exists( $renderer ) ) {
		return;
	}
	$classes = $repository::make()->get_by_ids( [ 'g-b5f3969' ] );
	$style = $classes['g-b5f3969'] ?? null;
	if ( ! $style ) {
		return;
	}
	// Extra specificity prevents plugin reset/default styles from replacing the shared class.
	$style['id'] = 'button-outline';
	$style['cssName'] = 'wpgb-facet button.wpgb-load-more.button-outline';
	$css = $renderer::make( \Elementor\Plugin::$instance->breakpoints->get_breakpoints_config() )
		->render( [ $style ] );
	wp_register_style( 'gcpro-wpgb-button-class', false );
	wp_enqueue_style( 'gcpro-wpgb-button-class' );
	wp_add_inline_style( 'gcpro-wpgb-button-class', $css );
}, 99 );

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

// Primary-service SVG is opt-in and renders only in Single Project2231 / 391017f8.
add_action( 'elementor/dynamic_tags/register', static function ( $manager ) {
	if ( ! class_exists( '\Elementor\Modules\AtomicWidgets\PropsResolver\Transformers\Svg_Src_Transformer' ) ) { return; }
	class GCPRO_Project_Hero_Service_Icon_Tag extends \Elementor\Core\DynamicTags\Data_Tag {
		private static $active = false;
		public function get_name() { return 'gcpro-project-hero-service-icon'; }
		public function get_title() { return 'Single Project Hero Primary Service Icon'; }
		public function get_group() { return 'post'; }
		public function get_categories() { return [ 'svg' ]; }
		public static function begin_icon( $element ) {
			if ( '391017f8' !== $element->get_id() || 'e-svg' !== $element->get_name() ) { return; }
			$document = \Elementor\Plugin::$instance->documents->get_current();
			self::$active = $document && 2231 === (int) $document->get_main_id();
		}
		public static function end_icon( $element ) {
			if ( '391017f8' === $element->get_id() ) { self::$active = false; }
		}
		public function get_value( array $options = [] ) {
			$empty = [ 'html' => '', 'url' => '' ];
			if ( ! self::$active ) { return $empty; }
			$id = get_the_ID();
			if ( 'gcpro_project' !== get_post_type( $id ) ) { return $empty; }
			$terms = get_the_terms( $id, 'project_service' );
			if ( empty( $terms ) || is_wp_error( $terms ) ) { return $empty; }
			// Match the existing text tag's selection policy without changing that tag.
			$selected = null;
			if ( class_exists( '\AIOSEO\Plugin\Common\Models\Post' ) ) {
				$primary = \AIOSEO\Plugin\Common\Models\Post::getPost( $id )->primary_term;
				$primary_id = is_object( $primary ) ? (int) ( $primary->project_service ?? 0 ) : 0;
				foreach ( $terms as $term ) {
					if ( $term->term_id === $primary_id ) { $selected = $term; break; }
				}
			}
			if ( ! $selected && 1 === count( $terms ) ) { $selected = reset( $terms ); }
			// Existing staging taxonomy IDs and approved Media Library SVGs only.
			$icons = [ 18 => 1438, 17 => 1439, 20 => 1440, 19 => 1441, 21 => 1442 ];
			$attachment = $selected ? ( $icons[ $selected->term_id ] ?? 0 ) : 0;
			if ( ! $attachment || 'image/svg+xml' !== get_post_mime_type( $attachment ) ) { return $empty; }
			return ( new \Elementor\Modules\AtomicWidgets\PropsResolver\Transformers\Svg_Src_Transformer() )->transform(
				[ 'id' => $attachment ],
				\Elementor\Modules\AtomicWidgets\PropsResolver\Props_Resolver_Context::make()
			);
		}
	}
	$manager->register( new GCPRO_Project_Hero_Service_Icon_Tag() );
	add_action( 'elementor/frontend/widget/before_render', [ 'GCPRO_Project_Hero_Service_Icon_Tag', 'begin_icon' ] );
	add_action( 'elementor/frontend/widget/after_render', [ 'GCPRO_Project_Hero_Service_Icon_Tag', 'end_icon' ] );
}, 20 );
