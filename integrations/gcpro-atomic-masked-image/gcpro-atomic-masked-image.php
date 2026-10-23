<?php
/**
 * Plugin Name: GCPRO Atomic Masked Image
 * Description: Independently editable photo and SVG mask for Elementor Atomic.
 * Version: 0.2.0
 * Requires Plugins: elementor
 */
if ( ! defined( 'ABSPATH' ) ) { exit; }

add_action( 'elementor/widgets/register', static function ( $manager ) {
	if ( ! class_exists( '\Elementor\Modules\AtomicWidgets\Elements\Base\Atomic_Widget_Base' ) ) { return; }
	require_once __DIR__ . '/masked-image.php';
	$manager->register( new \GCPRO\Atomic\Masked_Image() );
}, 20 );
