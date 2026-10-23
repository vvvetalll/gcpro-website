<?php
namespace GCPRO\Atomic;

use Elementor\Modules\AtomicWidgets\Elements\Base\Atomic_Widget_Base;
use Elementor\Modules\AtomicWidgets\Elements\Base\Has_Template;
use Elementor\Modules\AtomicWidgets\Controls\Section;
use Elementor\Modules\AtomicWidgets\Controls\Types\Image_Control;
use Elementor\Modules\AtomicWidgets\Controls\Types\Number_Control;
use Elementor\Modules\AtomicWidgets\Controls\Types\Select_Control;
use Elementor\Modules\AtomicWidgets\PropTypes\Classes_Prop_Type;
use Elementor\Modules\AtomicWidgets\PropTypes\Image_Prop_Type;
use Elementor\Modules\AtomicWidgets\PropTypes\Primitives\String_Prop_Type;
use Elementor\Modules\AtomicWidgets\PropTypes\Primitives\Number_Prop_Type;

if ( ! defined( 'ABSPATH' ) ) { exit; }

class Masked_Image extends Atomic_Widget_Base {
	use Has_Template;
	public static $widget_description = 'Photo with an independently replaceable SVG alpha mask.';
	protected $version = '0.1';
	public static function get_element_type(): string { return 'gcpro-masked-image'; }
	public function get_title() { return 'GCPRO Masked Image'; }
	public function get_icon() { return 'eicon-image'; }
	public function get_keywords() { return [ 'image', 'mask', 'photo', 'gcpro' ]; }
	public static function get_computed_html_tag( array $settings ): string { return 'div'; }
	protected static function define_props_schema(): array {
		return [
			'classes' => Classes_Prop_Type::make()->default( [] ),
			'photo' => Image_Prop_Type::make()->default_size( 'full' ),
			'mask' => Image_Prop_Type::make()->default_size( 'full' ),
			'mask_mode' => String_Prop_Type::make()->enum( [ 'none', 'svg' ] )->default( 'none' ),
			'fit' => String_Prop_Type::make()->enum( [ 'cover', 'contain' ] )->default( 'cover' ),
			'focal_x' => Number_Prop_Type::make()->default( 50 ),
			'focal_y' => Number_Prop_Type::make()->default( 50 ),
		];
	}
	protected function define_atomic_controls(): array {
		return [ Section::make()->set_label( 'Masked Image' )->set_id( 'content' )->set_items( [
			Image_Control::bind_to( 'photo' )->set_label( 'Photo' ),
			Image_Control::bind_to( 'mask' )->set_label( 'SVG Mask (select an SVG asset)' ),
			Select_Control::bind_to( 'mask_mode' )->set_label( 'Mask' )->set_options( [
				[ 'value' => 'none', 'label' => 'None — rectangular image' ],
				[ 'value' => 'svg', 'label' => 'SVG Mask' ],
			] ),
			Select_Control::bind_to( 'fit' )->set_label( 'Photo fit' )->set_options( [
				[ 'value' => 'cover', 'label' => 'Cover (crop)' ],
				[ 'value' => 'contain', 'label' => 'Contain (whole photo)' ],
			] ),
			Number_Control::bind_to( 'focal_x' )->set_label( 'Focal point X (%)' )->set_min( 0 )->set_max( 100 )->set_step( 1 ),
			Number_Control::bind_to( 'focal_y' )->set_label( 'Focal point Y (%)' )->set_min( 0 )->set_max( 100 )->set_step( 1 ),
		] ) ];
	}
	protected function get_templates(): array {
		return [ 'gcpro/atomic/masked-image' => __DIR__ . '/masked-image.html.twig' ];
	}
}
